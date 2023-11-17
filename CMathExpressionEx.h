/*******************************************************************************/
/*  Copyright (C) 2006 The SIMCAS project                                      */
/*                                                                             */
/*  This program is free software; you can redistribute it and/or modify       */
/*  it under the terms of the GNU General Public License as published by       */
/*  the Free Software Foundation; either version 2 of the License, or          */
/*  (at your option) any later version.                                        */
/*                                                                             */
/*  This program is distributed in the hope that it will be useful,            */
/*  but WITHOUT ANY WARRANTY; without even the implied warranty of             */
/*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              */
/*  GNU General Public License for more details.                               */
/*                                                                             */
/*  You should have received a copy of the GNU General Public License          */
/*  along with this program; if not, write to the Free Software                */
/*  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA. */
/*******************************************************************************/

#ifndef _EQUATIONEX_H_
#define _EQUATIONEX_H_

#include "MathExpression.h"

// class CDerivativeDataBase;
// class CNonLinDataBase;
// class CNonLinear;

// class CTransform
// {

// public:
//   typedef enum
//   {

//     TRANS,
//     AC,
//     DC

//   } TRANSFORM_TYPE;

//   TRANSFORM_TYPE m_Transform;
//   CElement *m_DerVariable;
// };

enum CAnalysisMode
{
  AC_ANALYSIS,
  TRANS_ANALYSIS,
  DC_ANALYSIS
};

class CMathExpressionEx : public CMathExpression
{
  // friend class CEquSystem;
private:
  OP_CODE m_op_hier;
  OP_CODE m_op_getv;

public:
  // void Add(const CMathExpression &equ) { BinaryOperation(CElementDataBaseEx::OP_ADD, equ); }
  // void Sub(const CMathExpression &equ) { BinaryOperation(CElementDataBaseEx::OP_SUB, equ); }
  // void Mul(const CMathExpression &equ) { BinaryOperation(CElementDataBaseEx::OP_MUL, equ); }
  // void Div(const CMathExpression &equ) { BinaryOperation(CElementDataBaseEx::OP_DIV, equ); }
  // void Add(const CElement *e) { BinaryOperation(CElementDataBaseEx::OP_ADD, e); }
  // void Sub(const CElement *e) { BinaryOperation(CElementDataBaseEx::OP_SUB, e); }
  // void Mul(const CElement *e) { BinaryOperation(CElementDataBaseEx::OP_MUL, e); }
  // void Div(const CElement *e) { BinaryOperation(CElementDataBaseEx::OP_DIV, e); }
  // void Simplify(const CElement *e) { BinaryOperation(CElementDataBaseEx::OP_SIMPLIFYELEM, e); }
  // void Simplify() { UnaryOperation(CElementDataBaseEx::OP_SIMPLIFY); }
  // void Neg() { UnaryOperation(CElementDataBase::OP_NEG); }
  // void MakeEval() { UnaryOperation(CElementDataBaseEx::OP_MAKEEVAL); }

  bool ToPython(CDisplay &ds, CAnalysisMode mode);
  // void Display(CDisplay &ds, bool bAll = true) const;
  pos_t DisplayBranch(CDisplay &ds, pos_t pos, unsigned priority = 0) const;
  // pos_t DisplayElement(CDisplay &ds, pos_t pos) const;
  pos_t DisplaySymbol(CDisplay &ds, pos_t pos, unsigned priority = 0) const;
  // pos_t DisplaySymbol(CDisplay &ds, pos_t pos, unsigned priority = 0) const;
  // void DisplaySymbolString(const char *sp, pos_t pos_array[CElementDataBase::MAX_PAR], unsigned precedence, CDisplay &ds) const;

  //   CElement *GetElement() const; // replaces reducetoelement
  //   bool IsForced() const { return GetVariable(false) == NULL; }
  //   bool IsNull() const { return (IsEmpty() || ((GetSize() == 1) && (Get(0) == CElementDataBase::OP_ZERO))); }
  //   bool IsEqualTo(const CMathExpressionEx &equ) const;
  //   CElementDataBaseEx *GetElementDB() const { return static_cast<CElementDataBaseEx *>(m_ElementDB); }
  //   CElement *GetVariable(bool bForced = false) const;
  //   bool HasVariable(OP_CODE op1) const;
  //   void ToPolynom(CElement *e);
  //   void BinaryOperation(OP_CODE op, const CElement *e1);
  //   void BinaryOperation(OP_CODE op, const CMathExpression &equ) { CMathExpression::BinaryOperation(op, equ); }

  //   void GetPower(const CMathExpressionEx &equ0, unsigned);
  //   void Instanciate(const CMathExpressionEx &equ1, const CElementArray &instance_list /*,  const CEquationArray* equ_list */);
  //   void Instanciate(const CMathExpressionEx &equ1, const CElement *e1, const CMathExpression *equ2);

  //   OP_CODE Pop(pos_t &pos) const { return CMathExpression::Pop(pos); }
  //   void Push(OP_CODE op) { CMathExpression::Push(op); }
  //   void Push(const CElement *e) { CMathExpression::Push(e); }
  //   void Push(const CMathExpression &equ) { CMathExpression::Push(equ); }
  //   //  void Push( const CValue& v )              { CMathExpression::Push( v ); }
  //   void Copy(const CMathExpressionEx &equ) { CMathExpression::Copy(equ); }
  //   void Zero() { CMathExpression::Zero(); }
  //   void CopyBranch(const CMathExpressionEx &equ, pos_t &pos)
  //   {
  //     Clear();
  //     PushBranch(equ, pos);
  //     RemoveZero();
  //   }
  //   bool GetFromString(CParser &IC) { return CMathExpression::GetFromString(IC); }
  //   void GetFromString(const char *s) { CMathExpression::GetFromString(s); }
  //   bool IsConst() const;
  //   void ChangeToIf();
  //   // void At( unsigned n );
  //   void Linearize(const CMathExpressionEx &equ1, CNonLinDataBase &ndb);
  //   void DisplayNull(CDisplay &ds) const
  //   {
  //     Display(ds);
  //     ds.Append("=0");
  //   }
  //   bool GetNullEquation(CParser &IC);
  //   void ExtractEquationList(CEquationArrayEx &list, OP_CODE separator = CElementDataBaseEx::OP_CONCAT) const;
  //   void ToEquation(const CEquationArrayEx &list, OP_CODE separator = CElementDataBaseEx::OP_SYST);
  //   void ApplyKirshoffLaws();
  //   void Replace(OP_CODE op1, OP_CODE op2) { CMathExpression::Replace(op1, op2); }
  //   const CValue &EvaluateCplx() const;
  //   const CValue &Evaluate() const;

  // private:
  //   void RemoveBiasPoint(); // goes with Diff transform
  //   void DiffTransformation(const CMathExpressionEx &equ, const CTransform &transform, CDerivativeDataBase *db);
  //   // unsigned DiffTransformation( const CMathExpressionEx& equ, const CTransform& transform, CDerivativeDataBase* db, unsigned pos );

  //   void AllForcedExcept(CElementArrayEx &elem_array) const;
  //   void Normalize();
  //   //  void VectorToEquation( const CMathExpression& equ );
  //   bool RemoveForcedBranches(CElementArray &elem_array, CEquationArrayEx &equ_array);
  //   bool IsSimple() const;
  //   unsigned GetUnknownNumber() const;
  //   void ApplyNonLinear(CNonLinear &non_lin);

public:
  // Copy Constructor
  // CMathExpressionEx(const CMathExpressionEx &equ) : CMathExpression(NULL) { Copy(equ); }
  CMathExpressionEx(CElementDataBase *edb = NULL) : CMathExpression(edb) {};
};
#endif